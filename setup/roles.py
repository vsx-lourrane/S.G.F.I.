import imp
from rolepermissions.roles import AbstractUserRole

class Fornecedor(AbstractUserRole):
    avaible_permissions= {
        'cadastrar_conta':True,
        'liberar_desconto':True,
        'cadastrar_fornecedor':True,
    }
    
class Usuario(AbstractUserRole):
    avaible_permissions= {
        'cadastrar_usuário':True,
        'gerenciar_contas':True,
     }
