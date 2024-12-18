import socket
import random
import time

SERVER_IP = "192.168.0.1"  # Nom du service Docker
SERVER_PORT = 12345
CHOICES = ["pierre", "papier", "ciseaux"]

def play_game():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((SERVER_IP, SERVER_PORT))
        print("Connecté au serveur")
        response = ""  # Initialisation de la variable response
        while response != "fin":
            choice = random.choice(CHOICES)
            client.send(choice.encode())
            print(f"Choix envoyé : {choice}")
            response = client.recv(1024).decode()
            print(f"Réponse du serveur : {response}")
            time.sleep(5)  # Attente avant le prochain choix

if __name__ == "__main__":
    play_game()
