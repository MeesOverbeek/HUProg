bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond hout', 'Helmond', 'Helmond brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldorp', 'Heeze', 'Weert'}

print('De volgende stations worden door beide trajecten aangedaan: {}'.format(', '.join(bruin.intersection(groen))))
print('De volgende stations op het bruine traject worden niet aangedaan door het groene traject: {}'.format(', '.join(bruin.difference(groen))))
print('De volgende stations worden door samen door de twee trajecten aangedaan: {}'.format(', '.join(bruin|groen)))