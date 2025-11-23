import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(async (context, next) => {
	const url = new URL(context.request.url);
	
	// Skip password check for login page and API routes
	if (url.pathname === '/login' || url.pathname.startsWith('/api/')) {
		return next();
	}
	
	// Check if user is authenticated via cookie
	const authCookie = context.cookies.get('authenticated');
	const isAuthenticated = authCookie?.value === 'true';
	
	if (!isAuthenticated) {
		// Redirect to login page
		return new Response(null, {
			status: 302,
			headers: {
				Location: '/login',
			},
		});
	}
	
	return next();
});

