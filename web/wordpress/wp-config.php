<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'root' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'OW$/`OV?>Hl@oU1vU(=4C$I.e).rYI0_tP_%(uk:M3e*[s7pZ$4n{<PWQ)mqYrr(' );
define( 'SECURE_AUTH_KEY',  '/OqgoHJ^P.V23Auy.c^cX2F[Nch~,`#<X-nb;b|hkA+?YrkWjX6!m6&Aiy.yQwR/' );
define( 'LOGGED_IN_KEY',    '%NDC(,_qT*d:-vT.tHn`FJ/hn8BIRBU6Y%#2;3d7T*!l5u#boKxc*VY~O ;ZAA}!' );
define( 'NONCE_KEY',        'FMxEy8lrQHl@r=mL<KT9[tb]7lX5>(=?,LMUl=+KcezgXQ`mD[h8OE,xtLxkc/Z%' );
define( 'AUTH_SALT',        '4it^a{$1ob[aeEb8?oh+fhINJJ*./MS9R5r<O9txx,O?fN?w dtXcbj4~`S$jo:>' );
define( 'SECURE_AUTH_SALT', 'b${BUjIb.l{a:D#{n#F3D*:~%Izx#X@ |rtZ+W wn(;H! MV%MY q_Kz-_#_|cyy' );
define( 'LOGGED_IN_SALT',   '~`1=:1W9<z/9.`0T yBQ5r1=XX0=n|y%!1Y=t3CS2@yv|d%=OP!%ZI.LZW#-JYK ' );
define( 'NONCE_SALT',       'aF0IGw:0cQ3L,j A1P UEy<<*pQ1>*Yk/,`,rEjsEOG}zUFJZ)mH&Ti^T_]Rceg6' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
