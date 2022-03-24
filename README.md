# IdO_2022

Ressources pour l'événement IdO 2022.

Pré-requis:

- Git
- Python3
- Nmap

```bash
git clone https://github.com/PatStLouis/IdO_2022.git && cd IdO_2022
python3 -m venv venv && . venv/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
chmod 600 id_ed25519
python script.py && cat final_score.json
```
