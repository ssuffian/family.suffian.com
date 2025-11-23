import type { APIRoute } from 'astro';

export const POST: APIRoute = async ({ request, cookies, redirect }) => {
	const { password } = await request.json();
	const correctPassword = import.meta.env.SITE_PASSWORD;
	
	if (!correctPassword) {
		return new Response(
			JSON.stringify({ error: 'Password not configured' }),
			{ status: 500 }
		);
	}
	
	if (password === correctPassword) {
		cookies.set('authenticated', 'true', {
			path: '/',
			maxAge: 60 * 60 * 24 * 30, // 30 days
			httpOnly: true,
			sameSite: 'strict',
			secure: import.meta.env.PROD,
		});
		return new Response(JSON.stringify({ success: true }), { status: 200 });
	}
	
	return new Response(
		JSON.stringify({ error: 'Incorrect password' }),
		{ status: 401 }
	);
};

