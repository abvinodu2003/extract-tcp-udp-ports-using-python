import pandas as pd

# Read the Excel file
df = pd.read_excel("ports.xlsx")  # change to your actual file name

# Normalize the text to uppercase to catch both TCP and UDP patterns
df['PORT'] = df['PORT'].astype(str).str.upper()

# Separate into TCP and UDP dataframes
tcp_df = df[df['PORT'].str.contains('TCP')]
udp_df = df[df['PORT'].str.contains('UDP')]

# Optional: remove rows that don't match either (if needed)
# other_df = df[~df['PORT'].str.contains('TCP|UDP')]

# Export to separate Excel files
tcp_df.to_excel("tcp_ports.xlsx", index=False)
udp_df.to_excel("udp_ports.xlsx", index=False)

print("✅ TCP and UDP port files created successfully!")

