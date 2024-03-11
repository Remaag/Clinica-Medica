# Listas vazias
funcionarios = ['Adolfo', 'Maria']
pacientes = []

class Funcionario:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    # Função para agendar uma consulta
    def agendar_consulta(self, paciente, data):
        print(f'''
            Paciente: {paciente}.
            Médico: {self.nome}.
            Data: {data}.
        ''')

    def realizar_exame(self, paciente):
        print(f'{self.nome} realizou uma consulta para o paciente {paciente}.')

class Medico(Funcionario):
    def __init__(self, crm):
        self.crm = crm

    def prescrever_medicamento(self, paciente, medicmaneto):
        print(f'{self.nome} (CRM: {self.crm}) prescreceu {medicmaneto} para o paciente {paciente}.')

class Enfermeiro(Funcionario) :
    def __init__(self, coren) :
        self.coren = coren

    def aplciar_injecao(self, paciente) :
        print(f'{self.nome} (COREN: {self.coren}) aplicou injeção no paciente {paciente}.')

    

while True:
    print (f''' {20 * '-'}
        Lista de ações do sistema:
        1 - Agendar consulta.
        2 - Prescrever medicamento.
        3 - Aplicar injeção.
        4 - Adicionar paciente.
        5 - Adicionar médico.
        6 - Adicionar infermeira.
        0 - Finalizar programa.
    ''')

    opcao = input ('Qual função deseja realizar?')

    if opcao == '1' :
        for iFuncionario in funcionarios:
            print(f'{iFuncionario}. funcionarios[iFuncionario]')
        iMedico = int( input('Escolha o numero do médico que atenderá a cunsulta.'))
        print (funcionarios[iMedico - 1])
        