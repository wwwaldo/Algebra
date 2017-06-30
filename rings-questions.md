---
layout: post
title: rings questions
categories: algebra
---

zero divisor:
element which multiplies to get the (additive) identity, ie.
u where uv = 0 or vu = 0, for nonzero v.
unit:
element which has a commutative multiplicative inverse; ie. u such that uv = vu = 1 in R. The set of units in R is denoted R^{\times}.


7.1: 1, 3, 4, 6, 13, 14*, 21, 25*, 26

Let R be a ring with (multiplicative) identity 1.

1. Show that (-1)^2 = 1 in R.

3. Let S be a subring of R, containing 1. Prove that if u is a unit in S, then u is a unit in R. Show by example that the converse is false.

Soln.
If uv = 1 with u, v in S, then uv = 1 with u, v in R, since S is a subset of R. 

The converse is false: see example (1).
The rationals are a ring and the integers are a subring.
However, the only units in Z are +-1. In particular, 2 is a unit
in Q, but not a unit in Z.

4. Prove that the intersection of any nonempty collection of subrings is also a subring.

6. Which are subrings?
* 
*
*
*
*
*

13. (Definition of nilpotent)
* Show that n = a^k * b for some a,b implies \bar{ab} is a nilpotent element of Z / nZ. (bar?)
* If a in Z is an integer, show that the element \bar{a} in Z/ nZ is nilpotent iff every prime divisor of n is also a divisor of a.
In particular, determine the nilpotent elements of Z / 72 Z explicitly.
* Let R be the ring of functions from a nonempty set X to a field F. Prove that R has no nonzero nilpotent elements.

14. (continued) Suppose x is nilpotent and R is commutative.
* Show x is either zero or a zero divisor.
* Show rx is also nilpotent.
* Show 1 + x is a unit.
* Show the sum of any nilpotent element and a unit is a unit.

Solution.
* Lol check the definition. x^k = 0, so x(x^k-1) = 0, valid as long as k > 0. If this holds, x is a zero divisor. Otherwise, x is 0.
* lolol use commutivity. do (rx)^k = r^k x^k by repeated applications of commutivity = r^k * 0 = 0 by property of 0.
* (Interesting!)
*

21. Let P(X) be the power set of X.

Defn. For A, B eles of P(X),
A + B = (A - B) \cup (B - A)
A \cross B = A \cap B
(so that A + B \cap A \cross B = \emptyvar always)

* Prove that P(X) is a ring under these operations.
Note: We call this a *ring of sets*.

Defn. R is Boolean if a^2 = a for all a in R (every element is idempotent). Note: every Boolean ring is commutative.=

* Prove that this ring is commutative, has an identity, and is Boolean.

25. Let I be the ring of integral Hamilton Quaternions, and define
N: I to Z by N(a + bi + cj + dk) = a^2 + b^2 + c^2 + d^2
(Note: N is called a norm.)

* Show that N(alpha) = alpha * \bar{alpha} for all alpha in I, where \bar{alpha} is the 'conjugate' of alpha (flip all the signs except for a's)

* Prove that N(alpha beta) = N(alpha) N(beta) for all alpha, beta in I
(norm preserves monoid operation)

* Prove that an element of I is a unit iff it has N(ele) = +1.
Show that I^\cross is isomorphic to the quaternion *group* of order 8 (the norm one quaternions!).
Note. The inverse in the ring of rational quaternions of a nonzero element alpha is \bar{alpha} / N(alpha).

26. (About *discrete valuations*.)