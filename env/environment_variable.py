from dotenv import load_dotenv
import os
import json

class GetEnv:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))

            with open(os.path.join(base_dir, '../enviroment.json'), 'r') as file:
                data = json.load(file)
                
                if data['enviroment'] == 'PROD':
                    print('============ AMBIENTE DE PROD ============')
                    load_dotenv(os.path.join(base_dir,'./.env.prod'))
                    
                else:
                    print('============ AMBIENTE DE DEV ============')
                    load_dotenv(os.path.join(base_dir,'./.env.dev'))
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def variable(self, var):
        print(os.getenv(var))  # for debug
        return os.getenv(var)