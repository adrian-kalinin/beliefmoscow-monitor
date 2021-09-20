from discord_webhook import DiscordWebhook, DiscordEmbed

import settings


def prepare_embed(product):
    embed = DiscordEmbed()

    total_stock = len(product['sizes'])
    price = product['sizes'][0]['price'].replace('.0', '')

    embed.set_title(product['title'])
    embed.set_url(product['link'])
    embed.set_thumbnail(url=product['image_url'])
    embed.set_description(f'Total stock: {total_stock}')
    embed.set_color('e74c3c')
    embed.set_footer(text='Belief')
    embed.set_timestamp()

    sizes_value = ''

    for size in product['sizes']:
        sizes_value += f'{size["title"]} [{size["quantity"]}]\n'

    embed.add_embed_field(name='Sizes', value=sizes_value)
    embed.add_embed_field(name='Price', value=price)
    embed.add_embed_field(name='Useful Links', value=f'[Cart]({settings.BASE_URL + settings.CART_PATH})')

    return embed


def send_message(embed):
    webhook = DiscordWebhook(url=settings.DISCORD_WEBHOOK_URL)
    webhook.add_embed(embed)
    webhook.execute()
