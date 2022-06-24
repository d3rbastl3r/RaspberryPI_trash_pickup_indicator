#!/usr/bin/python3

import click # https://click.palletsprojects.com/

@click.group()
def cli() -> None:
    """Provides the possibility to read the state and light up the LEDs

    Run 'COMMAND --help' for more information on a command
    """
    return

@cli.command('state')
@click.option('-a', '--activate', 'enable', is_flag=True, help='Activate the LED output if LEDs are deactivated')
def led_state(enable: bool) -> None:
    """Show the activation state (enabled or disabled)"""
    if enable:
        print('ENABLE :)')
        # TODO: Show the state
    
    # TODO: Read and show the state
    return

@cli.command('light', short_help='Light up the RGB LEDs')
@click.argument('pattern')
def set_led_light(pattern: str) -> None:
    """Enable the RGB LEDs according to given PATTERN.
    
    \b
    Possible PATTERN values:
    \b
        Binary f. e. 000_000_000_000_000_000_010_000
            - Consists of 8x3bit sections
            - LED / color will be turned on with a value "1" and turned off with a value "0"
            - Colors are assigned as follow: "RGB_RGB_RGB_..."
    \b
        Decimal f. e. 16
            - MIN: 0, MAX: 16.777.216
            - MSB is placed left
            - Value 16 is equivalent to 000_000_000_000_000_000_010_000
    \f
    
    :param str pattern: Pattern for the light of the LEDs
    """
    
    led_data = toInt(pattern)
    # TODO: Show given LED light pattern
    return

if __name__ == '__main__':
    cli()
