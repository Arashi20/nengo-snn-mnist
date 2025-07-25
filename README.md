# 🧠 Nengo Spiking Neural Network – MNIST Classifier

This project explores **Spiking Neural Networks (SNNs)** using the **Nengo** and **NengoDL** libraries, applied to the MNIST handwritten digit classification task.

## 🚀 Project Goals
- Build and train a spiking neural network using NengoDL
- Compare its performance with traditional ANNs
- Visualize spike activity and network behavior
- Experiment with biologically inspired mechanisms

## 📁 Project Structure
- `notebooks/`: Jupyter notebooks with code and visualizations
- `data/`: Any local datasets
- `scripts/`: Reusable Python functions or model code
- `results/`: Plots, logs, and spike activity recordings

## 🛠️ Requirements
```bash
pip install nengo nengo-dl tensorflow matplotlib
```

# HOW TO: Create/Activate a Virtual Environment
## Step 1: Create the virtual environment (once)
```bash
python -m venv venv
```


## Step 2: Activate it (every time you work on the project)
```bash
# On Windows
venv\\Scripts\\activate

# On macOS/Linux
source venv/bin/activate
```


## Step 3: Install packages inside the venv
```bash
pip install -r requirements.txt
```


# HOW TO: Commit & Push Changes to GitHub
```bash
# Step 1: Check what’s changed
git status

# Step 2: Stage specific files (example)
git add notebooks/my_notebook.ipynb

# Or stage all changes
git add .

# Step 3: Commit with a message
git commit -m "Describe what you changed"

# Step 4: Push to GitHub
git push origin main
```