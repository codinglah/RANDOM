# RANDOM

[![CodeFactor](https://www.codefactor.io/repository/github/codinglah/random/badge/main)](https://www.codefactor.io/repository/github/codinglah/random/overview/main)

## Update 16/1/22:

The `RanInt()` function has been improved, with `iterations` and `atype` combined into `avg`, and several bugs fixed.

### `RanInt(minimum, maximum, quantity = 1, avg = None)` 

#### Use

This function generates random integers within a predefined range, which are presented in a list.

##### `minimum`

The minimum number of the range.

##### `maximum`

The maximum number of the range.

##### `quantity`

How many random integers you want to generate. Default is `1`.

#### NOTE:

If you enter a decimal for any of the above arguments, it will **automatically be rounded** ***down*** **to the nearest integer**. For example, `3.9` gives `3`.

##### `avg`

Two values separated by `|`. First (ie before the `|`), how many random integers, whose average is taken afterwards, you want to generate. Second, the type of average you want to take from the previously mentioned integers generated. Available options are `mean`, `median`, `mode` and `rand`. `rand` randomly picks one of the averages.

An example for this would be `10|rand`, which generates random integers and takes 10 random averages of them.

**--**

Welcome to RANDOM! This package intends to provide a easy way to generate numbers, letters and more! Do note the following:

* This package is **not complete yet**. However, certain features are already available. You are welcome to test them, and please report issues while using them by creating an issue on this GitHub repository.
* To use this package, use `import RANDOM`. Do note that you have to **capitalize RANDOM**.

Last but not least, thank you for using **RANDOM**!

_codinglah_
