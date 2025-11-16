class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.is_engine_on = False

    def start_engine(self):
        if self.is_engine_on:
            print(f"{self.brand} {self.model} is already running.")
            return False
        
        self.is_engine_on = True
        print(f"{self.brand} {self.model} engine started.")
        return True
    
    def stop_engine(self):
        if not self.is_engine_on:
            print("Engine is already off")
            return False
        
        if self.speed > 0:
            print("Stop the car first!")
            return False
        
        self.is_engine_on = False
        print("Engine stopped")
        return True
    
    def accelerate(self, amount):
        try:
            if not self.is_engine_on:
                print("Start the engine first!")
                return False
            
            if amount <= 0:
                print("Acceleration must be positive!")
                return False
            
            self.speed += amount
            print(f"Accelerating... Current speed: {self.speed} km/h.")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def brake(self, amount):
        try:
            if amount <= 0:
                print("Brake must be positive!")
                return False
            
            if self.speed == 0:
                print("Car is already stopped.")
                return False
            
            self.speed = max(0, self.speed - amount)
            print(f"Braking... Current speed: {self.speed} km/h.")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_info(self):
        status = "Running" if self.is_engine_on else "Off"
        print(f"\n--- {self.brand} {self.model} ({self.year}) ---")
        print(f"Engine: {status}")
        print(f"Speed: {self.speed} km/h\n")

def main():

    car1 = Car("Tesla", "Model Y", 2018)

    # Accelerate without starting
    car1.accelerate(20)
    
    # Start and drive
    car1.start_engine()
    car1.accelerate(30)
    car1.accelerate(20)
    car1.get_info()
    
    # Brake
    car1.brake(25)
    car1.brake(30)  # Should stop at 0
    car1.get_info()
    
    # Try to stop engine while moving
    car1.accelerate(50)
    car1.stop_engine()  # Should fail
    car1.brake(50)
    car1.stop_engine()  # Should work
    
    # Multiple cars
    print("\n--- Testing Multiple Cars ---")
    car2 = Car("Tesla", "Model 3", 2023)
    car2.start_engine()
    car2.accelerate(100)
    car2.get_info()
    
    car1.get_info()  # car1 state unchanged

if __name__ == "__main__":
    main()
        