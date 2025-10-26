import random
class Citizen:
    def __init__(self,name):
        self.name=name
        self.energy_used=0
    def __str__(self):
        return f"{self.name} - Energy Used: {self.energy_used} kWh"
    

class Building:
    def __init__(self,building_name):
        self.building_name=building_name
        self.citizens=[]
        self.total_energy=0
    def add_citizen(self,citizen):
        self.citizens.append(citizen)
    def calculate_energy(self):
        for citizen in self.citizens:
            self.total_energy+=int(citizen.energy_used)
        return self.total_energy
    def __str__(self):
        return f"Building {self.building_name} | Total Energy: {self.calculate_energy()} kWh | Residents: {self.citizens}"
        
class City:
    def __init__(self,city_name):
        self.city_name=city_name
        self.buildings=[]
        self.city_energy=0
    def add_building(self,building):
        self.buildings.append(building)
    
    def simulate_day(self):
        for building in self.buildings:
            for citizen in building.citizens:
                citizen.energy_used=random.randint(1,10)
                # print(citizen)
            building.calculate_energy()
            self.city_energy+=building.total_energy
            # print(building)

    def generate_report(self):
        print(f"{self.city_name}")
        print(f"Total city energy: {self.city_energy} kWh")
        print(f"Total building: {len(self.buildings)}")
        for building in self.buildings:
            print(f"Building name: {building.building_name}")
            print(f"Energy usage per building {building.total_energy} kWh")
            highest_energy_consumers=sorted(building.citizens,key=lambda citizen:citizen.energy_used,reverse=True)
            i=0
            for highest_energy_consumer in highest_energy_consumers:
                i+=1
                print(highest_energy_consumer)
                if i==3:
                    break

city=City("Dhaka")
b1=Building("Skyline Tower")
b2=Building("Riverview Heights")

city.add_building(b1)
city.add_building(b2)

b1.add_citizen(Citizen("Durjoy"))
b1.add_citizen(Citizen("Anika"))
b1.add_citizen(Citizen("Farhan"))
b1.add_citizen(Citizen("Rafi"))
b1.add_citizen(Citizen("Tania"))

city.simulate_day()


city.generate_report()