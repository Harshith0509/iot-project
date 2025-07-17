import subprocess

def run_command(cmd):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(cmd, shell=True, text=True, check=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Output:\n", result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error:\n", e.stderr)
        return None

def pair_device():
    print("🔗 Pairing device...")
    pairing_cmd = (
        "./out/standalone/chip-tool pairing ble-wifi "
        "1234 SpectrumSetup-00B6 rarenight438 20070292 2257 "
        "--paa-trust-store-path ./credentials/development/paa-root-certs/"
    )
    run_command(pairing_cmd)

def turn_off_device():
    print("💡 Sending OFF command...")
    off_cmd = "./out/standalone/chip-tool onoff off 1234 1"
    run_command(off_cmd)

if __name__ == "__main__":
    pair_device()
    turn_off_device()
