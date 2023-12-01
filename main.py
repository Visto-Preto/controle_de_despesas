import json, os, sqlite3
from module.realsymbol import Real as rs
from module import platform

__author__ = 'VistoPreto'

os_cls, red, green, yellow, blue, magenta, cyan, reset, cmd_del = platform.platform()

class ControlDB():
	def __init__():
		pass
	def ver():
		if os.path.isfile('settings/data.db'):
			pass
		else:
			con = sqlite3.connect('settings/data.db')
			cur = con.cursor()
			cur.execute('''CREATE TABLE mov_atual(Desp1 REAL, Descr1 TEXT, Desp2 REAL, Descr2 TEXT)''')			
			cur.execute('''INSERT INTO mov_atual VALUES('{}', '{}', '{}', '{}')'''.format(0, '', 0, ''))
			con.commit()
			con.close()


class MainApp():
	def __init__(self):
		with open("settings/config.json", encoding='utf-8') as config:
			read_config = json.load(config)
			self.mes = read_config['mes']
			self.ano = read_config['ano']
			self.data1 = read_config['data1']
			self.data2 = read_config['data2']
			self.pagto1 = read_config['pagto1']
			self.pagto2 = read_config['pagto2']

	def run(self):
		os.system(os_cls)
		def print_values(x):
			x = rs.float_to_s(x)
			if x == None or x == '':
				x = ' R$ 0,00'

			x = ((14 - len(x)) * ' ' + x)
			return x
		trec = print_values(self.pagto1 + self.pagto2)


		print('=================================')
		print('       Controle de Despesas      ')
		print('=================================')
		print('    Pagto ref a {}/{}    '.format(self.mes, self.ano))
		print('  -----------------------------  ')
		print('       1º Recebimento do mês     ')
		print('{}        {}'.format(self.data1, print_values(self.pagto1)))
		print('Despeda           {}'.format(print_values(0)))
		print('Redimento         {}'.format(print_values(0)))
		print('  -----------------------------  ')
		print('      2º Recebimento do mês      ')
		print('{}        {} '.format(self.data2, print_values(self.pagto2)))
		print('Despesas          {}'.format(print_values(0)))
		print('Redimento         {}'.format(print_values(0)))
		print('  -----------------------------  ')
		print('              Resumo             ')
		print('Receita total     {}'.format(trec))
		print('Despesa total     {}'.format(print_values(0)))
		print('  -----------------------------  ')
		print('Rendimento total: {}'.format(print_values(0)))
		print('  -----------------------------  ')
		print('=================================')
		print('')
		print('1] Adicinar')
		print('2] Extrato')
		print('3] Config')
		print('0] Sair')
		op = input('\n ')
		os.system(os_cls)

ControlDB.ver()
MainApp().run()