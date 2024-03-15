import csv

file_names = []

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        file_names.append(row['File Name'])

file_paths = ['0008e7fe-cbaa-4381-a8e6-62e4577bdd93.txt', '01657715-6ad2-4d06-93f5-4dd334de4f0f.txt', '0214ab7f-6ccd-403a-a9c9-6a1f216e8989.txt', '025998db-e4f6-49fb-b888-061daef48197.txt', '0788aae6-6657-4ab9-9b54-d3901a07adaa.txt', '092f0e66-6112-4c0a-98fd-6be54477f26c.txt', '0acab36a-d8e2-4dff-893f-843f0ab30073.txt', '0ad69a47-a6d6-419f-80b7-7de2d4dab330.txt', '0c8fb35d-3c39-4401-bc91-eb0e5ff5bf0a.txt', '0d032927-990c-4d52-90ec-295e10c4ea55.txt', '0ea44e7a-ad8e-4d37-8bfd-6a27bcf38329.txt', '0f7c3d84-a441-47df-a646-2e0bdb9d848a.txt', '1557db39-e271-4ad4-a4b6-a64750d727b8.txt', '18b7e123-2d61-431e-9525-f6d73f3ea80e.txt', '1f16a406-e75c-4178-9f67-54ea687fffe2.txt', '2023a376-45ed-453a-9202-150df2986c51.txt', '2181b388-b4df-48bd-9937-ea29b1a1dfa1.txt', '249b84ee-ab42-4e24-bdeb-f7aea10087fd.txt', '24dedff0-c5c7-4abb-a8ab-e1846c0aeed7.txt', '262737ef-aa56-4705-bf42-442591509a0a.txt', '27dbce6b-3f0f-40db-8990-816be8a78447.txt', '3261f662-b5b1-40c5-968d-df7968cf464a.txt', '3801f047-e4ab-4597-91e0-723957c59b33.txt', '38f8d81c-6d78-4172-bba4-c112a6f757f7.txt', '3e19b332-b108-41d4-8a28-918631c52ca2.txt', '4076cd20-d9c6-4ada-ad53-f4c0a42a103c.txt', '434f82d7-a578-42e2-9b1a-4341892177c4.txt', '4d8e2d29-1fa7-4a9d-8cef-ed89d166c226.txt', '504acbd2-2413-41ae-897d-8ababcfb3542.txt', '541329cf-0eed-40bc-ad2f-9d0ab5202f87.txt', '57e8cb97-09e6-452c-908b-002c5f32446f.txt', '5e296f1f-613c-4120-b89f-9dd7f6d962d3.txt', '5ec0582b-2838-4f74-870b-518f9f2cb4c3.txt', '5ec9dc06-ef6c-4347-a1d1-dd9cc9707bed.txt', '5fe25b73-4c65-47ac-bed9-e2942781f928.txt', '618ea677-a244-4d6a-a98e-9496653def2c.txt', '61cce476-3016-41cb-8b36-1aec9098105b.txt', '64d5513b-cb1c-45e3-a161-14d13ab1819a.txt', '6908283b-755e-49e7-a499-5bd4b553b08c.txt', '6ae51a27-e299-4a1c-bd5a-169d9733c714.txt', '72c897c1-f553-4396-84f0-767cc2cb3405.txt', '73a38eff-373c-445d-842b-5262b477c1bb.txt', '7a1526e6-ab08-4e16-9a13-0b6743c1217e.txt', '7c74e1c4-a5dd-4cb6-915e-cce0d89d217d.txt', '7e1cdc4d-7692-477f-ba72-9414b5362227.txt', '80699d5f-df15-40a0-9e3c-48608a935ddd.txt', '8121dc2a-036f-4a99-bd33-24051d9cc3e7.txt', '86555281-f15b-4a48-b452-12bd95c2b03a.txt', '8b7b7831-cd05-4f37-9c0f-925631096a4c.txt', '8e839b08-b344-45c1-934a-f8268be52fa9.txt', '91c2420a-0660-4252-81b7-743fb5047867.txt', '94cc9374-a746-4af2-b97f-4b6c5e2ea6f4.txt', '99d59774-928d-44c0-b5e3-e115a40fce29.txt', '9abe8ee5-93d3-438f-8917-39b8acad8a58.txt', '9b218fd3-e2d4-42bc-a9cd-84865ceea7d4.txt', '9bb05dae-093b-4ba4-8760-daddc21ed94e.txt', '9fcf9576-fc65-4705-a242-60b5bfeea00a.txt', 'a3c30e21-5c6f-4d4d-8ec4-b9e0b4052d6f.txt', 'a43719c1-7450-4d4b-86cd-020665dea8cb.txt', 'a96f61e0-d1a8-44b7-bf2f-cccda20f15e3.txt', 'aec66da0-5420-44d5-ada6-1093f6046123.txt', 'b0d1d616-c605-4779-9cd6-7a26a905ed75.txt', 'bdd0a853-cac8-4fb5-a56f-316745d8cddd.txt', 'be7d96fc-296b-4db0-9367-fdcbd530c7ab.txt', 'c09df694-af1f-4b3f-8f52-e05bfb5e8674.txt', 'c0ab8b69-2f92-4618-9842-4f4d4b8a0496.txt', 'c1f54a02-2b5c-40ef-97d3-7c53983ba9b3.txt', 'c8901e48-181d-472b-87aa-c55edc72f9f9.txt', 'ca7771b0-d048-4631-bfce-1167b461313c.txt', 'cba86c0e-0492-47e8-9b36-27a60c9b81b3.txt', 'cc217880-cc43-4ab4-b91f-2795ec5a43d7.txt', 'cf5ccd33-f5fb-4619-ace7-372e0c219c97.txt', 'cf65ab18-45a2-47a0-821b-6d97ed0d7385.txt', 'd01be346-dd81-46ab-8727-298c0aed5086.txt', 'd24f7e89-f196-44f9-b830-a243504e9977.txt', 'd279e978-0f9b-4d2e-925e-692feebea701.txt', 'd2b705f5-15ab-456e-b4de-f56f2f98497f.txt', 'd4ac7d9e-f0c5-4b1e-9cc7-66c9499aa68a.txt', 'd7b89ddf-fbe6-41e6-a915-651717b1a79f.txt', 'da1bf77f-ed4c-4b74-960d-aebcff475b59.txt', 'e0e678c9-9dd5-401e-9bbf-dbaa70362829.txt', 'e236baec-c4c5-4024-9555-51517262662d.txt', 'e38ac3ce-d513-487e-b705-2d96799edcd2.txt', 'e5a1ec75-d235-40e9-9b2b-6a6c58fc927e.txt', 'e6fdd618-97ac-4260-ad6a-dfa82a2ffd6f.txt', 'e90ce3e0-f211-4ea7-965b-c3b86e6e9553.txt', 'ea88b135-2ff4-4557-971b-291a5d83541d.txt', 'eab48991-0a74-422e-a9fc-1bb6c1b8471e.txt', 'ecfc1154-e740-4972-aea6-ff60967fc2ea.txt', 'edf9e3e7-2767-424c-8260-c07414f5568d.txt', 'ef02a6b4-dc45-4cbc-b840-60b1b2df84c7.txt', 'f039c257-d537-4a93-9080-6df6bb92ae46.txt', 'f3e0da43-6b5b-48f3-99d9-dd364cc9ef48.txt', 'f496242a-9b38-436b-aac9-b49a6cbef783.txt', 'f5aa926e-b934-49f2-9803-235e75ac5eb0.txt', 'f72b9fa3-373e-400a-ace8-2af9dd95e003.txt', 'fc1c73cc-a71b-4410-bc92-ca62171ddb18.txt', 'fce936d0-647a-4707-bc90-d43ea25f3411.txt', 'fdf4b13d-2044-4f84-b7e7-f6c4da6f81f2.txt', 'fff127e0-47ff-4b5e-9a18-29662e1d9c5a.txt']



def find_unique_elements(list1, list2):
    # Create a set from the first list
    set1 = set(list1)

    # Create a set from the second list
    set2 = set(list2)

    # Find elements that are in set1 but not in set2
    unique_from_list1 = set1 - set2

    # Find elements that are in set2 but not in set1
    unique_from_list2 = set2 - set1

    # Print the unique elements from list1
    print("Elements present in list1 but not in list2:")
    for element in unique_from_list1:
        print(element)

    # Print the unique elements from list2
    print("\nElements present in list2 but not in list1:")
    for element in unique_from_list2:
        print(element)


find_unique_elements(file_paths,file_names)


def print_duplicates(lst):
    # Create a set from the list to store unique elements
    unique_elements = set(lst)

    # Iterate over the list
    for element in lst:
        # If the element appears more than once in the list
        if lst.count(element) > 1:
            # And it's not already printed (to avoid printing duplicates multiple times)
            if element in unique_elements:
                print(f"Duplicate element: {element}")
                # Remove the element from the set of unique elements
                unique_elements.remove(element)

print_duplicates(file_names)