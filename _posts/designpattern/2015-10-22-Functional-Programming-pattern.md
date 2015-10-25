---
layout: post
title: "Functional Patterns"
modified:
categories: [designpattern]
excerpt:
tags: [designpattern]
image:
  feature:
date: 2015-10-23T10:31:11+08:00
---

记录一个关于函数式设计模式

## Functional patterns
- Core Principles of FP design
  * Functions
  * Types
  * Composition
- Functions as parameters
  * Abstraction,Dependency injection
  * Partial application, Continuations,Folds
- Chaining Functions
  * Error handling, Async
  * Monads
- Dealing with wrapped data
  * Lifting,Functors
  * Validation with applicatives
- Aggregating data and operations
  * Monoids

## Functional programming is scary
- Functors
- applicatives
- currying
- catamorphism
- Monad
- Monoid
- chainable
- aggregatable
- mappable

## Object oriented programming is scary
- Generic
- Polymorphism
- Interface
- Inheritance
- SOLID: SRP,OCP,LSP,ISP,DIP,......
- Covariance
- IOC,DI,MVC

## OO Patterns VS FP Patterns
- OO pattern/principle
• Single Responsibility Principle
• Open/Closed principle
• Dependency Inversion Principle
• Interface Segregation Principle
• Factory pattern
• Strategy pattern
• Decorator pattern
• Visitor pattern

- FP pattern/principle
• Functions
• Functions
• Functions, also
• Functions
• Yes, functions
• Oh my, functions again! • Functions
• Functions

:)

## Functional programming
Haskell,OCaml, etc

## Core Principles of FP Design
- Steal from mathematics
- Types are not classes
- Functions are things
- Composition everytwhere

### Mathematics functions

• Input and output values already exist
• A function is not a calculation, just a mapping
• Input and output values are unchanged (immutable)

```
let add1 x = x+1
va1 add1: int->int
```

### Guideline: Strive for purity

```
￼let x = doSomething()
let y = doSomethingElse(x)
return y + 1
```
```
let helper() =
￼   let x = doSomething()
   let y = doSomethingElse(x)
   return y
return helper() + 1
```
- Laziness: only evaluate when I need output
- Cacheable results
  same answer every time – "memoization"
- No order dependencies
- Parallelizable  
- No Side Effects
- Immutable data

Haskell/Clojure

### Types are not classes
set of valid inputs and sets of valid output

Data Behavior Data

### Functions are things
A function is a standalone thing, not attached to a class.
Functions as inputs and outputs

### Composition everywhere
Types can be composed too
“algebraic types"

- Product type: *
  set of people * set of dates
- Sum type: +
  set of cash value + set of cheque value+ set of credit card value

### DDD & DOMAIN MODELING

to be continue ..........

发现函数式编程其实挺有意思的，函数式我觉的可以比面向对象更为抽象，所以他的代码少
是有道理的。




￼
