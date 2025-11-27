from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

def generate_username():
    # username format: word + 4 digits (example: cyber1234)
    words = ["cyber", "alpha", "nova", "pixel", "shadow", "code", "neo", "matrix", "CyberNovaX", "PixelRider", "ShadowByte", "NeonVortex", "AlphaRogue", "ByteHunter", "MysticPulse", "StormGlider", "DarkSpectra", "TechPhantom", "EchoReaper", "QuantumFrost", "BlazeRunner", "SilentMatrix", "AeroKnight", "NovaCipher", "PhantomShift", "ZeroSpecter", "HyperDrift", "NightCrawlerX", "SonicViper", "CyberWolfX", "PixelSamurai", "IronGalaxy", "StarBreaker", "FrostedBlade", "FlashVortex", "RapidNova", "GhostWielder", "SilverPhantom", "FireStormX", "RazorGlitch", "HexaWarrior", "NeonRaptor", "BlueShadowX", "TechSavior", "TurboBlaze", "IceReaper", "DarkHunterZ", "CyberVortex", "MysticFlare", "SilentNova", "SteelRanger", "AlphaSpectre", "QuantumAsh", "OmegaNexus", "NovaPulseX", "WildRaptor", "DarkVolt", "SonicCipher", "PixelWarlock", "TechRiderX", "ViperStorm", "ChaosGlider", "NeonDrifter", "FrostNova", "UltraKnightX", "CyberAshen", "BlazeSpectra", "PhantomVolt", "StarRaptorX", "ShadowBreaker", "MysticStorm", "IronPulse", "NovaViper", "SkyPhantom", "FrostRider", "ByteNinja", "NeonSpecter", "TechVandal", "SonicAsh", "ThunderCipher", "RazorPhantom", "PixelGlitch", "ShadowRover", "CyberRider", "PhoenixNova", "NightSpectra", "TurboCipher", "BlueVortex", "SteelGhost", "MysticVandal", "QuantumStorm", "NovaReaper", "DarkPulseX", "PixelVortex", "SonicSpecter", "TechGlitch", "NeonHunter", "MidnightCipher", "ByteWarrior", "AlphaNovaX", "SilverStorm", "RapidSpectra", "GhostCipher", "StormBreaker", "CyberSamurai", "FrostGlitch", "MysticDrifter", "ShadowNovaX"]
    word = random.choice(words)
    numbers = ''.join(random.choices(string.digits, k=4))
    return word + numbers

@app.route("/generate", methods=["GET"])
def generate():
    username = generate_username()
    return jsonify({"username": username})

@app.route("/")
def home():
    return jsonify({"message": "Random Username Generator API"})


if __name__ == "__main__":
    app.run(debug=False)
