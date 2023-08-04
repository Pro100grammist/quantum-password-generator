import numpy as np

from math import ceil


class QuantumGen:
    def __init__(self, length, character_set):
        self.length = length
        self.character_set = character_set

    @staticmethod
    def identity_gate():
        """Identity gate. Returns a 2x2 unit matrix"""
        return np.identity(2)

    @staticmethod
    def pauli_x_gate():
        """Pauli-X gate, which is a "NOT" operation for quantum bits. Returns the X-gate matrix."""
        return np.array([[0, 1], [1, 0]])

    @staticmethod
    def hadamard_gate():
        """Hadamard gate, used to create superpositions of states. Returns the Hadamard matrix."""
        return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

    @staticmethod
    def swap_gate():
        """A SWAP gate that swaps two quantum bits. Returns the matrix of the SWAP gate."""
        matrix = np.identity(4)
        matrix[[1, 2]] = matrix[[2, 1]]
        return matrix

    @staticmethod
    def controlled_x_gate():
        """A controlled X-gate that performs a NOT operation on the second bit if the first bit is 1.
        Returns the matrix of the controlled X-gate."""
        matrix = np.identity(4)
        matrix[[3, 2]] = matrix[[2, 3]]
        return matrix

    @staticmethod
    def apply(vector, *gates):
        """Calculating the final state vector of a quantum system after applying a sequence
        of quantum gates to the input state vector."""
        final_matrix = gates[0]
        remaining_gates = gates[1:]

        for gate in remaining_gates:
            final_matrix = np.kron(gate, final_matrix)

        resulting_vector = final_matrix.dot(vector)
        return resulting_vector

    @staticmethod
    def observe(v):
        """Measurement of the probability of each state by determining the squares of the
        moduls of the components of the state vector."""
        squared_probabilities = np.absolute(v) ** 2
        chosen_state_index = np.random.choice(v.size, 1, p=squared_probabilities)
        return chosen_state_index[0]

    @staticmethod
    def generate(self):
        """Generating a random bit by simulating the operation of a three-qubit quantum computer"""
        initial_state = np.array([1] + [0] * 7)  # create an initial state ( "|000⟩" )
        superposition_state = self.apply(initial_state, self.identity_gate(), self.hadamard_gate(), self.identity_gate())  # convert the 2nd qubit into superposition
        flipped_first_bit_state = self.apply(superposition_state, self.pauli_x_gate(), self.identity_gate(), self.identity_gate())  # change 1-th bit to 1 using the X-gate
        controlled_operation_result = self.apply(flipped_first_bit_state, self.controlled_x_gate(), self.identity_gate())  # confuse the 1st and 2nd cubits
        swapped_qubits_state = self.apply(controlled_operation_result, self.identity_gate(), self.swap_gate())  # swap the 2nd and 3rd cubits
        result = self.observe(swapped_qubits_state)  # observe qubits state

        return result

    def generate_password(self):
        """password generation"""
        password = ''
        while len(password) != self.length:
            random_number = int(''.join(['1' if self.generate(self) != 1 else '0' for _ in range(8)]), base=2)
            if random_number in self.character_set:
                password += (chr(random_number))

        return password

    def check_password_strength(self):
        """checking password strength against brute force attacks offline"""
        bruteforce_speed_per_second = 1000000  # Estimated password brute force speed
        password_complexity = len(self.character_set) ** self.length  # possible number of password combinations
        time_estimate = password_complexity / bruteforce_speed_per_second  # bruteforce password cracking time
        result = None

        if time_estimate < 1:
            result = "less than one second"
        elif time_estimate < 60:
            result = f"{int(time_estimate)} second"
        elif time_estimate < 3600:
            result = f"{int(time_estimate / 60)} minutes"
        elif time_estimate < 86400:
            result = f"{ceil(time_estimate / 3600)} hours"
        elif time_estimate < 31536000:
            result = f"{ceil(time_estimate / 86400)} days"
        else:
            result = f"The password is strong. Break-in time: approx {ceil(time_estimate / 31536000)} years " \
                     f"{ceil((time_estimate % 31536000) / 86400)} days"

        return result
