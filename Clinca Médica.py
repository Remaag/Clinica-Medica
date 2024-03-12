# Listas vazias
funcionarios = [{'nome': 'Raquel', 'especialidade': 'Cirurgião', 'crm': '294284'}]
pacientes = []

class Funcionario:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    # Função para agendar uma consulta
    def agendar_consulta(self, paciente, data):
        print(f'''
            Consulta agendada:
            Paciente: {paciente}.
            Data: {data}.
        ''')

    def realizar_exame(self, tipo_exame, paciente):
        print(f'Realizou um exame de {tipo_exame} para o paciente {paciente}.')


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


# Área de testes
medico = Funcionario(nome= 'Dr. João', especialidade= 'Cardiolistas')
medico.agendar_consulta(paciente= 'Maria', data= '10/10/2024')
medico.realizar_exame(tipo_exame= 'Eletrograma', paciente= 'Carlos') 

print(medico)
print(medico.agendar_consulta)
print(medico.realizar_exame)
   
# while True:
#     print (f''' {20 * '-'}
#         Lista de ações do sistema:
#         1 - Agendar consulta.
#         2 - Prescrever medicamento.
#         3 - Aplicar injeção.
#         4 - Adicionar paciente.
#         5 - Adicionar médico.
#         6 - Adicionar infermeira.
#         0 - Finalizar programa.
#     ''')

#     opcao = input ('Qual função deseja realizar?  ')

#     if opcao == '1' :
#         for i in range (0, len(funcionarios), 1):
#             print(f'{i + 1}. {funcionarios[i]}. \n')

#         iMedico = int( input('Escolha o numero do médico que atenderá a cunsulta.  '))
#         print (funcionarios[iMedico - 1])

#         iPaciente = input('Digite o nome do paciente.  ')
#         iData = input('Digite a data da consulta.  ')

#         Funcionario.agendar_consulta(iPaciente, iMedico, iData, iData)

        
#     if opcao == '2' :
#         pass