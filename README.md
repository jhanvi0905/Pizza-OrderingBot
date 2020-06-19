# Pizza_ordering_bot
Just a little implementation of your everyday to go pizza ordering bot which helps you order your customized choice of pizza.

# Natural Language Understanding Model for the bot:

1. Train data- different intents with slots annotated in each (data.md). The user intent is classified into 3 intents- greet, order_pizza, inform, done. Order_pizza- Intent when the user expresses an intent to order pizza while inform is for user answering the questions of bot in regards to customize the pizza to user likes.

2. Trianing- The backend of the trained entity and slot extraction model is specified in the configfile.yml. The trained model is present at models/nlu.

# Dialogue Generation Model

1. Train data- stories.md containing examples of what kind of conversation the user may have with the bot
2. Domain- P_domain.yml specifying all intents, slots and actions of the bots used in describing the stories in stories.md file.

# Actions:
The action templates for various kinds of reply on various user inputs are defined. However alongside, a fixed form action is also defined- responsible for attaining all the required information fields relating to pizza ordering by the bot. 

![Deployed Bot](https://github.com/jhanvi0905/Pizza-OrderingBot/blob/master/Screenshot%20(47).png)
![Deployed Bot](https://github.com/jhanvi0905/Pizza-OrderingBot/blob/master/Screenshot%20(48).png)
