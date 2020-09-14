class HelloWorld(object):
  """This class prints helloworld
  """
  def __init__(self, first_string):
  	self.first_string = first_string
  	second_string = 'Srija'
  	print('Hiiiiii')

  # def pretty_print(self):
  # 	print('%s %s' %(self._string, self._name))
  def printter(self, second_string):
    print(self.first_string,'World')
    print(second_string,'Hello')  


if __name__ == '__main__':
	printer = HelloWorld('heeee')
	# printer.pretty_print()
	printer.printter('World')
