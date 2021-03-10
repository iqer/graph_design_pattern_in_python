class Patient:

    def __init__(self, number) -> None:
        self._number = number

    def get_number(self):
        return self._number


class Hospital:
    def __init__(self, queue_size) -> None:
        self._patient_queue = [None] * queue_size
        self._last = 0
    
    def add_patient(self, patient):
        self._patient_queue[self._last] = patient
        self._last += 1
    
    def get_patient_at(self, index):
        return self._patient_queue[index]

    def get_queue_length(self):
        return self._last

    def iterator(self):
        return HospitalIterator(self)


class HospitalIterator:
    def __init__(self, hospital) -> None:
        self._hospital = hospital
        self._index = 0
    
    def has_next(self):
        if self._index < self._hospital.get_queue_length():
            return True
        return False
    
    def next(self):
        patient = self._hospital.get_patient_at(self._index)
        self._index += 1
        return patient.get_number()

    
if __name__ == '__main__':
    hospital = Hospital(4)
    hospital.add_patient(Patient('alice'))
    hospital.add_patient(Patient('boo'))
    hospital.add_patient(Patient('cat'))
    hospital.add_patient(Patient('dog'))
    it = hospital.iterator()
    while it.has_next():
        print(it.next())
