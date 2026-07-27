# Système de gestion e-commerce

## Description générale

Ce projet est une application e-commerce permettant à des **clients** d'acheter des produits en ligne et à un **administrateur** de gérer le catalogue, les commandes et les clients. Le système repose sur un modèle de données relationnel et sur un ensemble de fonctionnalités réparties entre deux types d'utilisateurs : le **Client** et l'**Admin**.

## Acteurs du système

### Client
Le client est un utilisateur final qui navigue sur la boutique, achète des produits et suit ses commandes.

**Actions possibles :**
- S'inscrire (créer un compte)
- Se connecter
- Consulter les produits par catégorie
- Ajouter des produits au panier
- Passer une commande
- Effectuer un paiement (inclus automatiquement dans le passage de commande)
- Suivre l'état de sa commande

### Admin
L'administrateur gère l'ensemble du back-office de la boutique.

**Actions possibles :**
- Se connecter (compte séparé du client)
- Gérer les produits (ajout, modification, suppression)
- Gérer les catégories de produits
- Gérer les commandes (suivi, mise à jour du statut)
- Gérer les clients (consultation, modération des comptes)
- Consulter les paiements effectués

## Modèle de données

Le système s'articule autour des entités suivantes :

| Entité | Attributs principaux | Rôle |
|---|---|---|
| **Cliente** | id_cliente, cliente_name, email, password, adresse | Représente un compte client, avec authentification et informations de livraison |
| **Admin** | id_admin, admin_name | Représente un compte administrateur |
| **Product** | id_product, product_name, price, quantity | Catalogue des produits disponibles à la vente |
| **Category** | id_categorie, category_name | Classification des produits |
| **Order** | id_order, order_date, total_amount, statut | Représente une commande passée par un client |
| **Paiement** | id_payment, payment_date, amount, statut | Représente le règlement associé à une commande |

## Relations entre entités

- Un **Client** peut passer **plusieurs commandes** (relation 1 → *).
- Une **Commande** est composée de **plusieurs produits**, chaque produit ayant une quantité et un prix associés à la ligne de commande.
- Une **Commande** entraîne **un paiement** (relation 1 → 1) une fois confirmée.
- Un **Produit** appartient à **une catégorie**, et une catégorie peut regrouper **plusieurs produits**.
- L'**Admin** gère les produits, catégories, commandes et clients, mais n'est pas directement lié aux commandes en tant qu'acheteur.

## Fonctionnement global

1. Le **client** crée un compte ou se connecte.
2. Il consulte le catalogue de produits, filtrable par catégorie.
3. Il ajoute des produits à son panier.
4. Il passe une commande, ce qui calcule le montant total (`total_calcul`) et déclenche la confirmation (`confirm()`).
5. La confirmation de commande **inclut** automatiquement l'étape de paiement (`Make_payment`).
6. Le statut de la commande et du paiement est mis à jour et peut être suivi par le client.
7. L'**administrateur**, de son côté, supervise l'ensemble du système : il alimente le catalogue (produits/catégories), suit les commandes et paiements, et gère les comptes clients.

## Diagrammes fournis

- **Diagramme de classes** : modélise les entités (Cliente, Admin, Order, Paiement, Product, Category) et leurs relations/cardinalités.
- **Diagramme de cas d'utilisation** : modélise les interactions des deux acteurs (Client, Admin) avec le système, y compris la relation `<<include>>` entre "Passer une commande" et "Effectuer un paiement".

## Pistes d'évolution possibles

- Ajout d'une gestion des rôles multiples pour l'Admin (super-admin, modérateur, etc.)
- Ajout d'un cas d'utilisation "Annuler une commande"
- Ajout d'un système d'avis/notes sur les produits
- Ajout d'une gestion des stocks avec alertes de rupture
