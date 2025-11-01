class Ensemble_Disjoint:

    def __init__(self, liste_objets: list):
        n = len(liste_objets)
        self.liste_indices = [i for i in range(n)]
        self.liste_tailles = [1 for _ in range(n)]

    def racine(self, indice: int):
        # Compression de chemin
        while indice != self.liste_indices[indice]:
            self.liste_indices[indice] = self.liste_indices[self.liste_indices[indice]]
            indice = self.liste_indices[indice]
        return indice

    def connection(self, idx: int, idy: int):
        racine_x = self.racine(idx)
        racine_y = self.racine(idy)

        if racine_x == racine_y:
            return  # déjà dans le même ensemble

        # Union par taille
        if self.liste_tailles[racine_x] >= self.liste_tailles[racine_y]:
            self.liste_indices[racine_y] = racine_x
            self.liste_tailles[racine_x] += self.liste_tailles[racine_y]
        else:
            self.liste_indices[racine_x] = racine_y
            self.liste_tailles[racine_y] += self.liste_tailles[racine_x]

    def connecté(self, idx: int, idy: int) -> bool:
        return self.racine(idx) == self.racine(idy)
