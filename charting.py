import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio
CHAIN = 'arbitrum'
# Read the CSV files and create a DataFrame for each token
tokens = ['DAI', 'USDC', 'FRAX', 'USDT',  'MIM', 'BUSD', 'USDD', 'MAI']
mainnet_tokens = ['DAI', 'USDC', 'USDT',  'MIM', 'BUSD']

dfs = {}
for token in tokens:

    file_path = f"data/{token.lower()}.csv"
    df = pd.read_csv(file_path, index_col=0)
    df['date'] = pd.to_datetime(df['updatedAt'], unit='s')
    df = df[['date', 'price']]
    df['date'] = pd.to_datetime(df['date'])
    df['price'] = df['price'] / 10 ** 8
    df.rename(columns={'price': f'price{token}'}, inplace=True)
    dfs[token] = df

# Merge all DataFrames into a single DataFrame
merged_df = pd.concat(dfs.values(), axis=1)
# merged_df = merged_df.query("date >= '2022-01-01'")

# Create the plot
fig = go.Figure()
fig.update_layout(template='plotly_dark')
for token, df in dfs.items():
    fig.add_trace(go.Scatter(x=df['date'], y=df[f'price{token}'], name=token))

fig.update_layout(title=F'{CHAIN.capitalize()} Stablecoin Oracle Data',
                  xaxis_title='Date',
                  yaxis_title='Price',
                  yaxis_tickprefix='$',
                  yaxis_tickformat=',.4f',
                  legend=dict(
                      orientation="h",
                      yanchor="bottom",
                      y=1.02,
                      xanchor="right",
                      x=1))

# Add an update menu to turn individual tokens on and off
buttons = []
for token in tokens:
    visible = [False] * len(tokens)
    visible[tokens.index(token)] = True
    button = dict(label=token,
                  method="update",
                  args=[{"visible": visible},
                        {"title": f"{token} Price"}])
    buttons.append(button)

fig.update_layout(updatemenus=[dict(type="buttons", buttons=buttons)])

# Export the plot to an HTML file
pio.write_html(fig, file="index.html", auto_open=True)
