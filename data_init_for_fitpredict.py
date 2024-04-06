import pandas as pd

lms_labels = ['0.NOSE', '9.mouth_left', '10.mouth_right', '11.left_shoulder', '12.right_shoulder', '13.left_elbow',
      '14.right_elbow', '15.left_wrist', '16.right_wrist', '17.left_pinky', '18.right_pinky', '19.left_index',
      '20.right_index', '21.left_thumb', '22.right_thumb', '23.left_hip', '24.right_hip', '25.left_knee',
      '26.right_knee', '27.left_ankle', '28.right_ankle', '29.left_heel', '30.right_heel', '31.left_foot_index',
      '32.right_foot_index']
columns = list()
for i in lms_labels:
    columns.append(f'x_{i}')
    columns.append(f'y_{i}')
    columns.append(f'z_{i}')


pd.DataFrame(columns=columns).to_csv('dataset_for_deadlift.csv', index=False)
