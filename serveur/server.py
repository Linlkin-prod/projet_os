import socket
import threading

# Dictionnaire pour stocker les connexions des clients et leurs choix
clients = {}

# Règles de Pierre-Papier-Ciseaux
RULES = {
    "pierre": {"ciseaux": "gagne", "papier": "perd"},
    "papier": {"pierre": "gagne", "ciseaux": "perd"},
    "ciseaux": {"papier": "gagne", "pierre": "perd"}
}

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "egalite"
    return RULES[choice1].get(choice2, "erreur")

def handle_client(conn, addr):
    print(f"Connexion de {addr}")
    clients[addr] = {"conn": conn, "choice": None}

    while True:
        try:
            # Réception du choix du client
            data = conn.recv(1024).decode()
            if not data:
                break

            print(f"Reçu de {addr} : {data}")
            clients[addr]["choice"] = data.strip().lower()

            # Vérifie si un match peut être organisé
            if len(clients) % 2 == 0 and all(c["choice"] for c in clients.values()):
                organize_match()
        except Exception as e:
            print(f"Erreur avec {addr}: {e}")
            break

    conn.close()
    print(f"Connexion fermée avec {addr}")
    del clients[addr]

def organize_match():
    # Récupère deux clients prêts à jouer
    client_list = list(clients.items())
    client1 = client_list[0]
    client2 = client_list[1]

    addr1, info1 = client1
    addr2, info2 = client2

    choice1 = info1["choice"]
    choice2 = info2["choice"]

    # Détermine le résultat
    result1 = determine_winner(choice1, choice2)
    result2 = "gagne" if result1 == "perd" else "perd" if result1 == "gagne" else "egalite"

    # Envoie les résultats aux deux clients
    info1["conn"].send(f"Votre choix: {choice1}, Adversaire: {choice2}, Resultat: {result1}".encode())
    info2["conn"].send(f"Votre choix: {choice2}, Adversaire: {choice1}, Resultat: {result2}".encode())

    # Réinitialise leurs choix
    info1["choice"] = None
    info2["choice"] = None

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))
    server.listen(4)
    print("Serveur en attente de connexions...")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
