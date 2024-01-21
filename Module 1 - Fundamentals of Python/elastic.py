import math
import toml


def get_properties(toml_file):
    """Read data from TOML file"""
    
    properties = toml.load("material_properties.toml")
    material = properties["material"]
    youngs_modulus = properties["elastic_properties"]["E"]
    poissons_ratio = properties["elastic_properties"]["nu"]
    density = properties["other_properties"]["rho"]
    
    return material, youngs_modulus, poissons_ratio, density


def get_moduli(youngs_modulus, poissons_ratio):
    """Calculate bulk and shear moduli from Young's modulus and Poisson's ratio"""
    
    # 1e-9 to convert to GPa
    bulk_modulus = 1e-9*youngs_modulus / 3 / (1 - 2*poissons_ratio)
    shear_modulus = 1e-9*youngs_modulus / 2 / (1 + poissons_ratio)
    
    return round(bulk_modulus, 2), round(shear_modulus, 2)


def get_shear_wavespeed(shear_modulus, density):
    """Calculate shear wavespeed from shear modulus and density"""
    
    # 1e9 to convert GPa to Pa
    return round(math.sqrt(shear_modulus*1e9 / density), 2)