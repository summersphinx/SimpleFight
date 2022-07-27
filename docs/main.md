# Main Commands

> help

Opens this Documentation in a browser.

## Loading

> load [*save name*]

Loads a different valid save if *save name* is given. If *save name* is not given, returns a list of all available saves.

> current-load

Returns the currently loaded save name (main characters name)

> start-load

Starts the currently loaded game.

## General In-game

> continue, cont

Continues to the next fight.

> items [*type*]

Returns a list of every item you currently have in your inventory. If *type* is given, sort for items with the specified tag. Tags are listed [here](https://github.com/summersphinx/SimpleFight/blob/master/tags.txt).

> use *item*

Use an item if that item is available.

> save

Saves the current game. By default, the game will auto save after every fight. Disable this with the setting GUI.

> settings

Opens the settings for the entire game. This will not control save specific settings.

> settings-save

Opens the settings for the individual save. This will not affect the general settings of the game.

> quit

Quits the game. This will only quit the game. ==Any unsaved progress will be lost!==
