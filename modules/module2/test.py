'''
    Manual/Visual Testing of Velocity
'''

import physics

def test_calculate_velocity(initial_velocity, distance, expected):
    '''
        Function to validate calculate_velocity()
    '''
    answer = physics.calculate_velocity( distance,initial_velocity)
    print(f'Input Vi = {initial_velocity}, distance = {distance}')
    print('expected = {} and Actual = {}'.format(expected,answer))


def main():
    test_calculate_velocity(0, 10, 14.00)
    test_calculate_velocity(0, 55.5, 32.98)

if __name__ == '__main__':
    main()
