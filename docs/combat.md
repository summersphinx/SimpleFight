# Combat

Combat is signified by the red background on the dialogue screen. The combat state will always load during any encounter.

```{attention}
Saving during combat is not allowed! Ensure either autosaves are enabled, or you have saved before entering combat to ensure you do not lose any progress.
```


## Stats

> me

Returns your player health, mana, and any status effects currently applied to you.


> enemy [*ID*]

Returns a guess of enemy health, mana, and potential status effects. If *ID* is given, returns stats for that enemy.
```{hint}
Status effects you have put on the enemy will be listed as potential effects.
```

```{hint}
*ID*'s start at 0.
```

```{error}
*ID* will only work when facing multiple enemies. Will error if facing only one enemy.
```

```{important}
*ID* of enemies will change when an enemy is killed if there is an enemy with a higher *ID*.
```


> items [*type*] [*name*]

Returns a list of every item you currently have in your inventory. If *type* is given, sort for items with the specified tag. Tags are listed [here](https://github.com/summersphinx/SimpleFight/blob/master/tags.md). If *name* is given, sort for items with the given name.

```none
items type=melee name=dagger
```

## Attacking

> atk, attack *weapon* *ID*

Attacks the specified target with the specified weapon. Target is identified with *ID*, while *weapon* is the item name. If you have multiple of one weapon selected, the first to be found will be used. Avoid this by renaming weapons, merging weapons[WIP], or selling old weapons at traders.
