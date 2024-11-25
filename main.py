from domain.create_file_log import LogFile
from env.environment_variable import GetEnv
import traceback 


def main():
    try:
        log = LogFile()
        variable = GetEnv()

        log.write_log('Construtores inicializado com sucesso')
        
        variable.variable('teste')
        
        
        log.write_log('Script executado com sucesso!!')

    except:
        print('>>> EXECUÇÃO APRESENTOU ERROS <<<')
        print(traceback.format_exc())
        log.write_log(f'== ERRO == \n{traceback.format_exc()} \n == END ERRO ==')
        

if __name__ == "__main__":
    main()

