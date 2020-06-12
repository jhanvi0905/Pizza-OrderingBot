from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory=trainer.persist(model_dir, fixed_model_name='pizzabotnlu')
print("training model")
train_nlu('./data/data.md', 'configfile.yml', './models/nlu')


interpret=Interpreter.load('./models/nlu/default/pizzabotnlu')
def ask_ques(text):
    print(interpret.parse(text))
ask_ques("Hello")
ask_ques("I want to order a thin crust Margharita Pizza")
ask_ques("Capsicum and extra cheese")
ask_ques("Okay")
ask_ques("2")