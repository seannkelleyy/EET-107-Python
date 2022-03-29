# Sean Kelley
# Ch10-1
# 20 July 2021

print('Describe your computer')

user_cpu = input("How fast is your computer's CPU in Ghz?: ")
user_ram = input('How much RAM does your computer have in GB?: ')
user_drive = input('How much drive space does your computer have in GB?: \n')
class Computer:
    def __init__(self, cpu, ram, drive):
        self.cpu = cpu
        self.ram = ram
        self.drive = drive
    def displayspecs(self):
        print(f'The computer has a CPU running at {self.cpu} Ghz')
        print(f'It has {self.ram} GB of RAM and has {self.drive} GB of storage available.')

user_computer = Computer(user_cpu, user_ram, user_drive)
user_computer.displayspecs()