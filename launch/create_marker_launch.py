import yaml

from simple_launch import SimpleLauncher

def generate_launch_description():
    sl = SimpleLauncher()
    
    params = sl.find('create_display_marker', 'marker_coordinates.yaml')
    print(params)
    
    with open(params) as file:
        try:
            data = yaml.safe_load(file)   
            #print(data)
            nodes=[]
            text_list = []
            for key, value in data.items():
                nodes.append(key)
                text_list.append(value)
        except yaml.YAMLError as exc:
            print("error during the read of YAML file")
    #print(nodes)
    #print(text_list)
    values_array=[]
    i=0
    for text in text_list:
        #print(text)
        values_array.append([])
        text_list_n = text.split(':')
        for new_text in text_list_n:
            valid_text = new_text.split(' ')
            values_array[i].extend(valid_text)
            #print(valid_text)
        i=i+1
    print(values_array)
    for i in range(len(nodes)):
        l_arg = [values_array[i][2*n+1] for n in range(len(values_array[i])//2)] #only take the even indexes, because the other correspond to 'x','y',etc... and the node only take values arguments
        #print(l_arg)
        #print(len(values_array[i])//2)

        sl.node("tf2_ros", "static_transform_publisher",name=nodes[i],arguments=l_arg)
                    
    return sl.launch_description()

