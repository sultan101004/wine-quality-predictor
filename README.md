\# Wine Quality Predictor - MLOps Assignment



\## 📋 Assignment Requirements Demonstrated



✅ \*\*CI/CD Pipeline\*\* with GitHub Actions  

✅ \*\*Admin approval workflow\*\* for pull requests  

✅ \*\*Automated testing\*\* with pytest and flake8  

✅ \*\*Branch protection rules\*\* enforcing workflow  

✅ \*\*Group collaboration\*\* with admin approval  

✅ \*\*Three-branch strategy\*\* (dev → test → main)  



\## 🛠️ Tools Used

\- GitHub \& GitHub Actions

\- Python, Flask, Scikit-learn

\- Docker (ready for Jenkins)

\- Pytest, Flake8



\## 📊 Workflow Demonstration

1\. Feature branch → PR to dev (requires admin approval)

2\. dev → PR to test (requires approval + tests passing)  

3\. test → PR to main (requires approval + tests passing)



\## 🚀 Jenkins Ready

The `Jenkinsfile` is configured for containerization and Docker Hub push



File Structure: 



├── app/

│   ├── \_\_init\_\_.py

│   ├── model.py

│   ├── predict.py

│   └── templates/index.html

├── tests/

│   ├── test\_app.py

│   └── test\_model.py

├── .github/workflows/

│   ├── ci.yml

│   └── cd.yml

├── .gitignore

├── Dockerfile

├── Jenkinsfile

├── README.md

├── requirements.txt

└── train\_model.py



