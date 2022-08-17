from rohdeschwarz.instruments.genericinstrument import GenericInstrument


# connect
instr = GenericInstrument()
instr.open_tcp('localhost')

instr.timeous_ms = 5_000

# open log
instr.open_log('instr.log')
instr.print_info()

# clear errors
instr.clear_status()

# preset
instr.preset()
instr.pause()


# TODO: insert code here
# for example:
instr.write('INIT')
instr.query('*OPC?')
data = instr.query('FETC?')
print(data)


# errors?
for error_code, message in instr.errors():
    print(f'error {error_code}: {message}')

input('Press <Enter> to continue.')
