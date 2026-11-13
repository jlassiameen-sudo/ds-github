# Gestionnaire de Tâches

A simple command-line task manager written in Python. It lets you add, view, search, and edit tasks from a text menu.

## Features

- **Add a task** with a title, a description, and a priority
- **Display all tasks** in a numbered list
- **Search tasks** by keyword (matches title or description, case-insensitive)
- **Edit a task** by its number
- **Input validation**: rejects non-numeric input, empty fields, and priorities outside 1–3

## Requirements

- Python 3.x
- No external libraries needed

## How to Run

```bash
python Amen_allah_jlassi_projet.py
```

## Usage

When the program starts, the following menu is displayed:

```
GESTIONNAIRE DE TACHES
1 : ajouter une tache
2 : afficher les taches
3 : rechercher une tache
4 : modifier une tache
0 : quitter
```

Type the number of the action you want and press Enter.

| Choice | Action |
|--------|--------|
| 1 | Add a new task (title, description, priority) |
| 2 | Show all tasks |
| 3 | Search tasks by keyword |
| 4 | Edit an existing task by its number |
| 0 | Quit the program |

### Priority levels

| Value | Meaning |
|-------|---------|
| 1 | Low |
| 2 | Medium |
| 3 | High |

### Example

```
Votre choix : 1
Titre : Buy groceries
Description : Milk, bread, eggs
Priorite (1=basse, 2=moyenne, 3=haute) : 2
Tache ajoutee.

Votre choix : 2
1 - Buy groceries | priorite : 2
      Milk, bread, eggs
```

## Project Structure

```
Amen_allah_jlassi_projet.py   # Entire program (functions + main loop)
README.md
```

### Main functions

- `saisir_entier`, `saisir_texte`, `saisir_priorite`: validated user input
- `ajouter_tache`, `afficher_taches`, `rechercher_tache`, `modifier_tache`: task operations
- `afficher_menu` / `main`: menu display and main loop

## Notes

- Tasks are stored in memory only, so they are lost when the program exits.

## Author

Amen Allah Jlassi
