# Numerical Integration with Simpson's and Trapezoidal Methods

This repository contains Python code for numerical integration using Simpson's and Trapezoidal methods. Both composite and normal implementations are provided.

## Description

Numerical integration is a method to approximate the definite integral of a function. Simpson's and Trapezoidal methods are popular numerical integration techniques used to compute the area under a curve.

### Simpson's Rule

Simpson's rule approximates the integral of a function by approximating the area under the curve with quadratic approximations. It is more accurate than the Trapezoidal rule and requires fewer evaluations of the integrand.

### Trapezoidal Rule

The Trapezoidal rule approximates the integral of a function by approximating the area under the curve with trapezoids. Although it is less accurate than Simpson's rule, it is easier to implement and can still provide reasonable results.

### Composite Methods

Composite methods involve dividing the integration interval into smaller subintervals and applying the corresponding method to each subinterval. This approach is often used to improve accuracy and efficiency, especially for functions with varying behavior.

## Usage

The Python code in this repository provides implementations of numerical integration using Simpson's and Trapezoidal methods, both composite and normal.

### Dependencies

- Python 3.x
- NumPy (for array operations)
- Pandas
- matplotlib (For visulation)

### Running the Code

To run the provided Python script, simply execute it in a Python environment:

To use The normal version When n=1 Version of Simpson's And Trapezoidal

```bash
python Simpson_Traperzoid.py
```

To use The Composite Version of Simpson's And Trapezoidal

```bash
python Simpson_Traperzoid_Composite.py
```
And There is A solution Of An Exercice That Calculating The Speed According To Data Given (Time And Accelaration Using the composite Version of Simpson And Trapezoidal)

```bash
python Ex02.py
```

