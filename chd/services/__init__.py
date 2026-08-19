from .paciente_service import (
    remover_paciente,
    cadastro_paciente,
    
)

from .lerDados import (
    exibirDados
)

from .medico_service import (
    cadastro_medico
)
from .buscarDados import (
    buscarFuncionario, buscarPaciente
)

from .agendamento_service import (
    gerar_agendamento,
    gerador_de_agendamentos_validos
)

from .atualizarDados import (
    menuAtualizar,
    atualizar_Dados
)