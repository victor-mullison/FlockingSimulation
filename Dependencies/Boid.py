
import tkinter as tk
from Dependencies.Vector2 import Vector2
import random


# Boid class extends the tkinter widget class so it can be displayed
class Boid(tk.Label): 
    def __init__(self, root, image):
        # Sprite display
        super().__init__(root, image=image)
        
        # For flocking behaviour
        self.perceptionRadius = 30
        self.position = Vector2(random.randint(0,500), random.randint(0,500))
        self.velocity = Vector2(random.randint(-5,5), random.randint(-5,5))
        self.acceleration = Vector2(0,0)
        self.maxSpeed = 3
        self.maxForce = 1
    
    def edges(self):
        if self.position.x > 500:
            self.position.x = 0
        elif self.position.x < 0: 
            self.position.x = 500
        if self.position.y < 0:
            self.position.y = 500
        elif self.position.y > 500:
            self.position.y = 0
            
    def align(self, flock):
        steering = Vector2(0,0)
        total = 0
        
        for boid in flock:
            if boid == self:
                continue
            
            dist = self.position.distance_to(boid.position)
            if dist <= self.perceptionRadius:
                steering += boid.velocity
                total += 1
            
        if total > 0: 
            steering  = steering / total
            steering.setMag(self.maxSpeed)
            steering -= self.velocity
            steering.limit(self.maxForce)
            
        return steering
    
    def cohesion(self, flock):
        steering = Vector2(0,0)
        total = 0
        
        for boid in flock:
            if boid == self:
                continue
            
            dist = self.position.distance_to(boid.position)
            if dist <= self.perceptionRadius * 2:
                steering += boid.position
                total += 1
            
        if total > 0: 
            steering = steering / total
            steering -= self.position
            steering.setMag(self.maxSpeed)
            steering -= self.velocity
            steering.limit(self.maxForce)
            
        return steering
    
    def separation(self, flock):
        steering = Vector2(0,0)
        total = 0
        
        for boid in flock:
            if boid == self:
                continue
            
            dist = self.position.distance_to(boid.position)
            if dist <= self.perceptionRadius:
                diff = self.position - boid.position
                diff = diff /  dist * dist
                steering += diff
                total += 1
            
        if total > 0: 
            steering = steering / total
            steering.setMag(self.maxSpeed)
            steering -= self.velocity
            steering.limit(self.maxForce)
            
        return steering
    
    def set_multipliers(self, al, co, sep):
        self.al_mult = al / 100
        self.co_mult = co / 100 / 2
        self.sep_mult = sep / 100
        
    def flock(self, flock):
        alignment = self.align(flock)
        cohesion = self.cohesion(flock)
        separation = self.separation(flock)
        
        alignment *= self.al_mult
        cohesion *= self.co_mult
        separation *= self.sep_mult
        
        self.acceleration += alignment
        self.acceleration += cohesion
        self.acceleration += separation
        
                
    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration
        self.velocity.limit(self.maxSpeed)
        self.acceleration = Vector2() # Reset to zero each update