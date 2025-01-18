from netmiko import ConnectHandler

# Configuration du routeur
router = {
    "device_type": "cisco_ios",
    "ip": "192.168.232.131",  # Adresse IP du routeur
    "username": "maher",
    "password": "maherssh",
    "secret": "enablepass"  # Mot de passe enable
}

# Connexion au routeur
print("Connexion au routeur...")
connection = ConnectHandler(**router)
connection.enable()

# Configurer une interface loopback
print("Configuration de l'interface Loopback111...")
commands = [
    "conf t"
    "interface Loopback111",
    "ip address 10.111.111.111 255.255.255.0",
    "no shutdown"
]
config_output = connection.send_config_set(commands)

# Afficher la sortie de configuration
print("Sortie de configuration :")
print(config_output)

# Déconnexion
connection.disconnect()
print("Configuration terminée et déconnexion.")