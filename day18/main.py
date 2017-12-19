#!/usr/bin/env python

registers = {}

def get_value(val):
    try:
        return int(val)
    except:
        return get_value(registers[val])

def play(instructions):
    
    last_sound = 0
    i = 0
    while i < len(instructions):
        instruction = instructions[i].strip()
        
        command = instruction[:3]
        register = instruction[4]
        value = instruction[6:]

        if not register in registers:
            registers[register] = 0

        if command == 'snd':
            last_sound = get_value(register)
        elif command == 'set':
            registers[register] = value
        elif command == 'add':
            val = get_value(value)
            registers[register] = get_value(register) + val
        elif command == 'mul':
            val = get_value(value)
            registers[register] = get_value(register) * val
        elif command == 'mod':
            val = get_value(value)
            registers[register] = get_value(register) % val
        elif command == 'rcv':
            if get_value(register) > 0:
                print(last_sound)
                break
        elif command == 'jgz':
            if get_value(register) > 0:
                i += get_value(value)
                continue
        
        i+=1

if __name__ == '__main__':
    f = open('/Users/kosta/dev/advent-of-code-17/day18/input.txt', 'r')
    instructions = f.readlines()
    f.close()
    play(instructions)