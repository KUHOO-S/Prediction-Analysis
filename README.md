# Prediction-Analysis
## Prediction based Telegram Bot for Temperature ,Water Quality and AQI.


ChatBot system with the following functionalities. It will provide three details, weather prediction, air quality index prediction and water quality prediction. Predictive analytics plays a central role in deriving value from the real-time data of IoT industry. Many companies rely on this predictive analysis of their assets to get a sustainable market edge. Chatbots are of the more advantageous applications of this. While being complex and incorporating AI, they also give the ease of implementation and a great user experience.

The dataset for this project is taken from [data.gov.in](https://data.gov.in) .The website provides real-time dataset through APIs and also dataset in .csv format. For implementation purposes , all datasets have been trimmed to a time frame of one year (2019-2020).


### Run the project

1. Clone the repo
```sh
git clone https://github.com/KUHOO-S/Prediction-Analysis.git
cd Prediction-Analysis
```
2.Change "BOT TOKEN" in kbot.py file to your telegram bot token
3. Run the .ipynb files to get result csvs' or directly run the bot
```sh
python kbot.py
```
### Future aspects:

The scope of this project can further be extended to including mobile app development,wherein the app is specifically designed to cater to the needs of the user in a more secluded fashion, as opposed to using a bot API for an already existing app.For the purposes of this project demonstration, the datasets used were comparatively smaller and resulted in lesser accuracy. Moving the project to cloud(like Microsoft Azure suite) can provide us better accuracy on using a larger dataset.

### References

1. Haupt,SueEllen,etal."Machinelearningforappliedweatherprediction."​2018IEEE14th International Conference on e-Science (e-Science)​. IEEE, 2018.
1. Chen,Sheng,etal."InvestigatingChina'sUrbanAirQualityUsingBigData,InformationTheory,andMachineLearning."​PolishJournalofEnvironmentalStudies27.2 (2018).
1. Haghiabi,AmirHamzeh,AliHeidarNasrolahi,andAbbasParsaie."Waterqualitypredictionusingmachinelearningmethods."​WaterQualityResearchJournal53.1(2018): 3-13.
1. https://medium.com/@mayankshah1607/machine-learning-feature-selection-with-backward-elimination-9558946540267
1. https://www.kaggle.com/hiteshsoneji/historical-weather-data-for-indian-cities
