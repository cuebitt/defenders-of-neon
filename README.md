<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/defenders-of-neon/master/game/gui/window_icon.png" alt="Defenders of Neon">
</p>

# Defenders of Neon

![release](https://img.shields.io/github/v/release/remarkablegames/defenders-of-neon)
[![build](https://github.com/remarkablegames/defenders-of-neon/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/defenders-of-neon/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/defenders-of-neon/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/defenders-of-neon/actions/workflows/lint.yml)

📖 Write visual novels with Defenders of Neon.

Play the game:

- [remarkablegames](https://remarkablegames.org/defenders-of-neon)

Or download:

- [Windows](https://github.com/remarkablegames/defenders-of-neon/releases/latest/download/win.zip)
- [Mac](https://github.com/remarkablegames/defenders-of-neon/releases/latest/download/mac.zip)
- [Linux](https://github.com/remarkablegames/defenders-of-neon/releases/latest/download/pc.zip)

## Credits

### Art

- [Uncle Mugen](https://lemmasoft.renai.us/forums/viewtopic.php?t=17302)

### Audio

- [Kenney](https://kenney.nl/assets/interface-sounds)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/defenders-of-neon.git
cd defenders-of-neon
```

Rename the project:

```sh
git grep -l "Defenders of Neon" | xargs sed -i '' -e "s/Defenders of Neon/My Novel/g"
```

```sh
git grep -l 'defenders-of-neon' | xargs sed -i '' -e 's/defenders-of-neon/my-novel/g'
```

Replace the assets:

- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`
- [ ] [`icon.icns`](https://anyconv.com/png-to-icns-converter/)
- [ ] [`icon.ico`](https://anyconv.com/png-to-ico-converter/)
- [ ] `web-icon.png`
- [ ] `web-presplash.webp`

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
