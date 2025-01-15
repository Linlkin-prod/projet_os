import socket
import random
import time


SERVER_IP = "serveur"  # Nom du service Docker
SERVER_PORT = 12345
CHOICES = ["pierre", "papier", "ciseaux"]

def play_game():
    print("Lancement du jeu")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        response = ""
        client.connect((SERVER_IP, SERVER_PORT))
        print("Connecté au serveur")
        while response != "fin":
            choice = random.choice(CHOICES)
            client.send(choice.encode())
            print(f"Choix envoyé : {choice}")
            response = client.recv(1024).decode()
            print(f"Réponse du serveur : {response}")
            time.sleep(5)  # Attente avant le prochain choix

if __name__ == "__main__":
    try:
        play_game()
    except Exception as e:
        print(f"Erreur: {e}")
        play_game()
