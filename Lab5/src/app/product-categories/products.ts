export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  link: string;
  imglink: string;
  rating: number;
  category_id: number;
  isActive: boolean;
  likes: number;
}

export const products = [
  {
    id: 1,
    name: 'Apple iPhone 11 128Gb Slim Box',
    price: 650,
    description: 'A large phone with one of the best screens',
    link: 'https://kaspi.kz/shop/p/apple-iphone-11-128gb-slim-box-chernyi-100692388/?c=750000000#!/item',
    imglink: 'https://cdn.dsmcdn.com/ty460/product/media/images/20220623/13/129227848/505450588/1/1_org_zoom.jpg',
    rating: 8.9,
    category_id: 1,
    isActive: true,
    likes: 1042,
  },
  {
    id: 2,
    name: 'Samsung S23',
    price: 809,
    description: 'A great phone with one of the best cameras',
    link: 'https://kaspi.kz/shop/p/samsung-galaxy-s23-ultra-5g-12-gb-512-gb-zelenyi-podarok-108714425/?c=750000000#!/item',
    imglink: 'https://i.ytimg.com/vi/1A4-WVhDFzc/maxresdefault.jpg',
    rating: 9.2,
    category_id: 1,
    isActive: true,
    likes: 1222,
  },
  {
    id: 3,
    name: 'OPPO A17',
    price: 299,
    description: '',
    link: 'https://kaspi.kz/shop/p/oppo-a17-4-gb-64-gb-chernyi-107420168/?c=750000000#!/item',
    imglink: 'https://www.mobihall.com/data/mobile/2018/11/Oppo%20RX17%20Neo_dd56.jpg',
    rating: 7.3,
    category_id: 1,
    isActive: true,
    likes: 13042,
  },
  {
    id: 4,
    name: 'Air cleaner ARNICA Hydra Rain Plus',
    price: 250,
    description: 'Perfect for people suffering from allergies. ',
    link: 'https://kaspi.kz/shop/p/arnica-hydra-rain-plus-krasnyi-3700837/?c=750000000#!/item',
    imglink: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h2f/hda/68829486022686/arnica-hydra-rain-plus-krasnyi-3700837-1.jpg',
    rating: 4.3,
    category_id: 3,
    isActive: true,
    likes: 942,
  },
  {
    id: 5,
    name: 'Iron Vitek VT-8304',
    price: 50,
    description: 'This is a powerful and reliable model of a home iron that meets the basic requirements and is equipped with all the necessary functions for your convenience.',
    link: 'https://kaspi.kz/shop/p/vitek-vt-8304-chernyi-3800548/?c=750000000#!/item',
    imglink: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h7a/h70/31593847128094/vitek-vt-8304-cernyj-sinij-3800548-1-Container.jpg',
    rating: 5.3,
    category_id: 3,
    isActive: true,
    likes: 1282,
  },
  {
    id: 6,
    name: 'Apple MacBook Air 13',
    price: 960,
    description: 'A small chip. A grand breakthrough is the first chip designed specifically for Mac.',
    link: 'https://kaspi.kz/shop/p/apple-macbook-air-13-mgn63-seryi-100797845/?c=750000000#!/item',
    imglink: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h65/h0f/33125684084766/apple-macbook-air-2020-13-3-mgn63-seryj-100797845-1-Container.jpg',
    rating: 9.3,
    category_id: 2,
    isActive: true,
    likes: 9042,
  },
  {
    id: 7,
    name: 'Sony PlayStation 5',
    price: 700,
    description: 'Dream of a teen gamer',
    link: 'https://kaspi.kz/shop/p/sony-playstation-5-god-of-war-ragnar-k-107674130/?c=750000000#!/item',
    imglink: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h45/hf2/66015013568542/sony-playstation-5-god-of-war-ragnarok-107674130-1.jpg',
    rating: 8.9,
    category_id: 2,
    isActive: true,
    likes: 11042,
  },
  {
    id: 8,
    name: 'ASUS TUF Gaming A15',
    price: 738,
    description: '',
    link: 'https://kaspi.kz/shop/p/asus-tuf-gaming-a15-fa506ihrb-hn084-90nr07g7-m008c0-chernyi-106255184/?c=750000000#!/item',
    imglink: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h6b/h33/62100002701342/asus-tuf-gaming-a15-fa506ihrb-hn084-90nr07g7-m008c0-cernyj-106255184-1.jpg',
    rating: 6.4,
    category_id: 2,
    isActive: true,
    likes: 10642,
  },
  {
    id: 9,
    name: 'Moccasins',
    price: 13,
    description: 'The one who gets it does not regret it.',
    link: 'https://kaspi.kz/shop/p/monika-moda-n-4-zelenyi-36-105308213/?c=750000000#!/item',
    imglink: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/he3/hf4/51542669230110/monika-moda-n-4-zelenyj-105308205-1.jpg',
    rating: 10,
    category_id: 4,
    isActive: true,
    likes: 10412,
  },
  {
    id: 10,
    name: 'Washer LG F2J3HS4L',
    price: 450,
    description: 'Unlike conventional washing machines, the LG drum has a wide range of rotation options, maximally adapted to different types of fabric and the degree of contamination of laundry',
    link: 'https://kaspi.kz/shop/p/lg-f2j3hs4l-serebristyi-3601603/?c=750000000#!/item',
    imglink: 'https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h2e/h56/31753168060446/lg-f2j3hs4l-serebristyj-3601603-1.jpg',
    rating: 4.5,
    category_id: 3,
    isActive: true,
    likes: 10472,
  },
];

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
